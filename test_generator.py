"""Generated passwords should never change, these unit tests can assure this
with reasonable accuracy"""

from generator import generate_password
import pytest


def test_pass_key_pairs():
    assert generate_password("foo", "bar", 20) == "DebatesTechnologyNorthern3;"
    assert (
        generate_password("yes", "no", 30)
        == "HandedEmergencyFuneralLocations1^"
    )
    assert generate_password("passw0rd", "google", 10) == "ClinicShould2<"
    assert generate_password("letmein", "gmail", 15) == "RelativesWorlds8+"
    assert generate_password("secret", "key", 100) == (
        "PredictedMortgageMuslimsBalancedWeeksOrderedEducationPositions"
        "StageFancyPieceProducedRachelAdvocates2("
    )


@pytest.mark.parametrize("target_len", [10, 20, 40, 60, 80])
def test_pass_len(target_len):
    assert len(generate_password("foo", "bar", target_len)) >= target_len
    assert len(generate_password("asdf", "qwerty", target_len)) >= target_len

