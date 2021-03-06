from django import forms
from django.core.exceptions import ValidationError
from sim.models import JobIdModel
import gettext


class ValueForm(forms.Form):
    ARG_TYPE_CHOICE = (
        ('r', 'Range'),
        ('v', 'List of values'),
    )
    type = forms.ChoiceField(label="Type of argument", choices=ARG_TYPE_CHOICE)
    name = forms.CharField(label="Element name", max_length=50)
    args = forms.CharField(label="Arguments", max_length=300)

    def is_valid(self):
        valid = super(ValueForm, self).is_valid()

        if not valid:
            return valid

        # Checking the args for range field
        if self.cleaned_data['type'] == 'r':
            argslist = self.cleaned_data['args'].replace(' ', '').split(',')
            # Checking if num of args is exactly 3
            if len(argslist) != 3:
                valid = False
                self.add_error('args', ValidationError(
                    gettext.gettext('Invalid number of arguments, expected 3, got %(num)s'),
                    code='invalid_num_args',
                    params={'num': len(argslist)}))
            else:
                # Checking if all of args are integer
                for arg in argslist:
                    try:
                        int(arg)
                    except ValueError:
                        valid = False
                        self.add_error('args', ValidationError(
                            gettext.gettext('Invalid type of arguments, expected integer'),
                            code='invalid_type_args'))
        elif self.cleaned_data['type'] == 'v':
            # Nothing special for arbitrary values so far
            pass
        return valid


class AddFileForm(forms.Form):
    file = forms.FileField(label="Upload file")
    name = forms.CharField(label="Include in the args as", max_length=50, required=False)


class JobForm(forms.Form):
    job_name = forms.CharField(label='Job Name:', max_length=300)
    exec_file = forms.FileField(label="Upload executable")
    arg_template = forms.CharField(label="Argument template", max_length=300)

    def is_valid(self):
        valid = super(JobForm, self).is_valid()
        if not valid:
            return valid
        for job in JobIdModel.objects.all():
            if self.cleaned_data['job_name'] == job.job_name:
                valid = False
                self.add_error('job_name', ValidationError(
                            gettext.gettext('This name already exists'),
                            code='duplicate_job_name'))
                break
        return valid


