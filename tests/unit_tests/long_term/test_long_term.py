import responses  # https://github.com/getsentry/responses

from verda.long_term import LongTermPeriod, LongTermService

PERIODS_PAYLOAD = [
    {
        'code': '1-month',
        'name': '1 Month',
        'is_enabled': True,
        'unit_name': 'month',
        'unit_value': 1,
        'discount_percentage': 5,
    }
]


class TestLongTermService:
    @responses.activate
    def test_get_periods(self, http_client):
        endpoint = http_client._base_url + '/long-term/periods'
        responses.add(responses.GET, endpoint, json=PERIODS_PAYLOAD, status=200)

        service = LongTermService(http_client)

        periods = service.get()

        assert isinstance(periods, list)
        assert len(periods) == 1
        assert isinstance(periods[0], LongTermPeriod)
        assert periods[0].code == '1-month'
        assert periods[0].discount_percentage == 5
        assert responses.assert_call_count(endpoint, 1) is True

    @responses.activate
    def test_get_instance_periods(self, http_client):
        endpoint = http_client._base_url + '/long-term/periods/instances'
        responses.add(responses.GET, endpoint, json=PERIODS_PAYLOAD, status=200)

        service = LongTermService(http_client)

        periods = service.get_instances()

        assert len(periods) == 1
        assert periods[0].unit_name == 'month'
        assert responses.assert_call_count(endpoint, 1) is True

    @responses.activate
    def test_get_cluster_periods(self, http_client):
        endpoint = http_client._base_url + '/long-term/periods/clusters'
        responses.add(responses.GET, endpoint, json=PERIODS_PAYLOAD, status=200)

        service = LongTermService(http_client)

        periods = service.get_clusters()

        assert len(periods) == 1
        assert periods[0].is_enabled is True
        assert responses.assert_call_count(endpoint, 1) is True
