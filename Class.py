class attractions:
  def __init__(self, address, website, tags, image, name, loc):
    self.address = address
    self.website = website
    self.tags = tags
    self.image = image
    self.name = name
    self.loc = loc


  def get_data(self):
    return [self.address, self.website, self.tags, self.image, self.name, self.loc]

