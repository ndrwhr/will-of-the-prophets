"""Board tests."""

# pylint: disable=redefined-outer-name, unused-argument

import pytest


@pytest.mark.django_db
@pytest.mark.parametrize("url", ["/", "/roll_frequency/"])
def test_public(client, url):
    """Test that pages do not require authorization."""
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("url", ["/roll/"])
def test_requires_auth(client, admin_client, url):
    """Test that pages require authorization."""
    response = client.get(url)
    assert response.status_code == 302
    response = admin_client.get(url)
    assert response.status_code == 200
