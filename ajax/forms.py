from django import forms
from boothManagement.models import Booth_Owner, Product_Details, Advertisements_order


class UploadImageForm(forms.ModelForm):
	def clean(self):
		super(UploadImageForm, self).clean()
		this_file = self.files
		fileType = this_file['image'].content_type
		fileSize = this_file['image'].size
		if fileType not in ['image/jpg', 'image/jpeg', 'image/png']:
			raise forms.ValidationError("This format is not supported!")
		if fileSize > 5242881:  # 5 MB
			raise forms.ValidationError("The image size is too big!")
		return self.cleaned_data

	def save(self):
		if not self.instance.image == self.instance.image.field.default:
			self.instance.image.delete(save=True)
		obj = super(UploadImageForm, self).save()
		file = self.files['image']
		obj.image.save(file.name, file.file)
		obj.save()
		return obj


class UploadBoothImageForm(UploadImageForm):
	class Meta:
		model = Booth_Owner
		fields = ('image',)


class UploadProductImageForm(UploadImageForm):
	class Meta:
		model = Product_Details
		fields = ('image',)


class UploadAdvertisementsImageForm(UploadImageForm):
	class Meta:
		model = Advertisements_order
		fields = ('image',)
