from dataclasses import dataclass

from dataclasses_json import dataclass_json

LONG_TERM_PERIODS_ENDPOINT = '/long-term/periods'


@dataclass_json
@dataclass
class LongTermPeriod:
    """Long-term pricing period returned by the public API."""

    code: str
    name: str
    is_enabled: bool
    unit_name: str
    unit_value: float
    discount_percentage: float


class LongTermService:
    """Service for interacting with long-term pricing periods."""

    def __init__(self, http_client) -> None:
        self._http_client = http_client

    def get(self) -> list[LongTermPeriod]:
        """Return all long-term periods."""
        periods = self._http_client.get(LONG_TERM_PERIODS_ENDPOINT).json()
        return [LongTermPeriod.from_dict(period) for period in periods]

    def get_instances(self) -> list[LongTermPeriod]:
        """Return long-term periods available for instances."""
        periods = self._http_client.get(f'{LONG_TERM_PERIODS_ENDPOINT}/instances').json()
        return [LongTermPeriod.from_dict(period) for period in periods]

    def get_clusters(self) -> list[LongTermPeriod]:
        """Return long-term periods available for clusters."""
        periods = self._http_client.get(f'{LONG_TERM_PERIODS_ENDPOINT}/clusters').json()
        return [LongTermPeriod.from_dict(period) for period in periods]
