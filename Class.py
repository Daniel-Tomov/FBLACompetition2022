class attractions:
  def __init__(self, address, website, tags, image, name, long, lat):
    self.address = address
    self.website = website
    self.tags = tags
    self.image = image
    self.name = name
    self.long = long
    self.lat = lat


  def get_data(self):
    return [self.address, self.website, self.tags, self.image, self.name, self.long, self.lat]

