import json
from pydantic import BaseModel, TypeAdapter, Field
from typing import Optional

__all__ = ["Ksynk"]


class KsynkFileRules(BaseModel):
    lines: int | list[int] = Field(title="Line(s) of code")


class KsynkFileItem(BaseModel):
    source_file: str | list[str] = Field(title="Source file(s)")
    destinations: list[str | tuple[str, KsynkFileRules]] = Field(
        description="A list of files, can be specific for a certain file")


class KysnkSchema(BaseModel):
    files: list[KsynkFileItem] = Field(title="Files")


class Ksynk(BaseModel):
    name: str = Field(description="Name of your ruleset")
    git_url: str = Field(title="Git URL")
    rules: list[KysnkSchema] = Field(description="A set of rules for checking")
    local_path: Optional[str] = Field(
        title="Local path", description="A local file path to the repo its associated from")


def main():
    ksynk_schema = TypeAdapter(Ksynk)

    with open("ksynk_schema.json", "+w", encoding="utf-8") as f:
        json.dump(ksynk_schema.json_schema(), f, indent=2)


if __name__ == "__main__":
    main()
