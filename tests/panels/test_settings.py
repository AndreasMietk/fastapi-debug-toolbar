from fastapi import status

from ..decorators import override_panels
from ..testclient import TestClient


@override_panels(["debug_toolbar.panels.settings.SettingsPanel"])
def test_settings(client: TestClient) -> None:
    store_id = client.get_store_id("/async")
    response = client.render_panel(store_id, "SettingsPanel")

    assert response.status_code == status.HTTP_200_OK
    assert "PANELS" in response.json()["content"]