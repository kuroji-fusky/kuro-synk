from dataclasses import dataclass

__all__ = ["Ksynk"]


@dataclass
class KsynkFileRules:
    lines: int | list[int]


@dataclass
class KsynkFiles:
    source_file: str
    destinations: list[str | tuple[str, KsynkFileRules]]


@dataclass
class KysnkSchema:
    git_url: str
    local_path: str
    files: list[KsynkFiles]


Ksynk = list[KysnkSchema]
