class attractions:
  def __init__(self, address, website, tags, image, name, longi, lat):
    self.address = address
    self.website = website
    self.tags = tags
    self.image = image
    self.name = name
    self.longi = longi
    self.lat = lat


  def get_data(self):
    return [self.address, self.website, self.tags, self.image, self.name, self.longi, self.lat]

