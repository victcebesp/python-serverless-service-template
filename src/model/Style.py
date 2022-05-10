import uuid


class Style:
    def __init__(self, name, description, owner_id, s3_url, layers, base_style_url, style_id=uuid.uuid4()):
        self.style_id = style_id
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.s3_url = s3_url
        self.layers = layers
        self.base_style_url = base_style_url
