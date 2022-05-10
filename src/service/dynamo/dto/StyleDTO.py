class StyleDTO:
    def __init__(self, PK, SK, name, description, owner_id, s3_url, layers, base_style_url, style_id):
        self.PK = PK
        self.SK = SK
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.s3_url = s3_url
        self.layers = layers
        self.base_style_url = base_style_url
        self.style_id = style_id
