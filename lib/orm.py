class ModelMixin:
  def to_dict(self, ignore_fileds = ()):
    '''将一个model转换成为一个字典'''
    attr_dict = {}
    for field in self._meta.fields:
      name = field.attname
      if name not in ignore_fileds:
        attr_dict[name] = getattr(self, name)
    return attr_dict