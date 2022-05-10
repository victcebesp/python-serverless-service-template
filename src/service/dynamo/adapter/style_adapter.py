from src.service.dynamo.dto.StyleDTO import StyleDTO
from src.model.Style import Style


def toDTO(style):
    return StyleDTO(
        f"USER{style.owner_id}",
        f"STYLE{style.style_id}",
        style.name,
        style.description,
        style.owner_id,
        style.s3_url,
        style.layers,
        style.base_style_url,
        style.style_id,
    )

def toModel(style_dto):
    return Style(
        style_dto.name,
        style_dto.description,
        style_dto.owner_id,
        style_dto.s3_url,
        style_dto.layers,
        style_dto.base_style_url,
        style_dto.style_id,
    )
