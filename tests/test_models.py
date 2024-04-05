#!/bin/bash
# -*- Mode: python -*-
import json

from ..enkanetwork.enum import EquipmentsType
from ..enkanetwork.model.equipments import Equipments


with open("tests/test.json", "r") as f:
    _j = json.load(f)


def test_artifacts() -> None:
    """
    Test case 2:
        Test equipments star
    """

    for star in _j["artifacts"]:
        raw = _j["artifacts"][star]
        data = Equipments.model_validate(raw)
        assert data.id == raw["itemId"]
        assert data.type in list(EquipmentsType)
        assert data.detail.name is not None
        assert data.detail.icon is not None
        assert data.detail.icon.url.startswith("https://")
        assert data.detail.rarity != 0
        assert data.level == raw["reliquary"]["level"] - 1

        # Stats
        assert data.detail.mainstats is not None
        assert data.detail.mainstats.prop_id != ""
        assert data.detail.mainstats.name is not None

        if len(data.detail.substats) > 0:
            for sub in data.detail.substats:
                assert sub.prop_id != ""
                assert sub.name is not None


def test_weapons():
    """
    Test case 3:
        Test weapons star
    """

    for star in _j["weapons"]:
        raw = _j["weapons"][star]
        data = Equipments.model_validate(raw)
        assert data.id == raw["itemId"]
        assert data.type in list(EquipmentsType)
        assert data.detail.name is not None
        assert data.detail.icon is not None
        assert data.detail.icon.url.startswith("https://")
        assert data.detail.rarity != 0
        assert data.level == raw["weapon"]["level"]

        # Stats
        assert data.detail.mainstats is not None
        assert data.detail.mainstats.prop_id != ""
        assert data.detail.mainstats.name is not None

        if len(data.detail.substats) > 0:
            for sub in data.detail.substats:
                assert sub.prop_id != ""
                assert sub.name is not None

        assert data.level == raw["weapon"]["level"]
        if "affixMap" in raw["weapon"]:
            assert (
                data.refinement
                == raw["weapon"]["affixMap"][list(raw["weapon"]["affixMap"].keys())[0]]
                + 1
            )
