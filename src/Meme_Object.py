class Meme_Object:
    """
        This represents a single one liner item retrieved from the URL_CONFIG file
        Config file must have following format:
        element, value, url
    """
    #
    def __init__(self, line):
        line_list = line.split(",")
        element, value, url = line_list[0], line_list[1], line_list[2]
        self.element = str.strip(element)
        self.value = str.strip(value)
        self.url = str.strip(url)
    #
    def get_element(self):
        return self.element
    #
    def get_value(self):
        return self.value
    #
    def get_url(self):
        return self.url