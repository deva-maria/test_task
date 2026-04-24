# Проверка метода GET
def test_get_disk_info_returns_200(client):
    response = client.get_disk_info()

    assert response.status_code == 200, (
        f"Ожидал код 200, но пришёл {response.status_code}. Ответ: {response.text}"
    )
    assert "total_space" in response.json(), "В ответе нет поля total_space"

# Проверка метода PUT и GET
def test_put_create_folder_and_get_it(client, folder_path):
    create_response = client.create_folder(folder_path)
    assert create_response.status_code in (201, 409), (
        f"Папка не создалась. Код: {create_response.status_code}. "
        f"Ответ: {create_response.text}"
    )

    get_response = client.get_resource(folder_path)
    assert get_response.status_code == 200, (
        f"После создания папка не открывается. Код: {get_response.status_code}. "
        f"Ответ: {get_response.text}"
    )

    cleanup_response = client.delete_resource(folder_path, permanently=True)
    assert cleanup_response.status_code in (204, 202, 404), (
        f"Не получилось почистить тестовые данные. Код: {cleanup_response.status_code}. "
        f"Ответ: {cleanup_response.text}"
    )

# Проверка метода POST
def test_post_move_folder(client, created_folder):
    moved_path = f"{created_folder}_moved"

    try:
        move_response = client.move_resource(created_folder, moved_path)
        assert move_response.status_code in (201, 202), (
            f"Папка не переместилась. Код: {move_response.status_code}. "
            f"Ответ: {move_response.text}"
        )

        if move_response.status_code == 201:
            moved_get = client.get_resource(moved_path)
            assert moved_get.status_code == 200, (
                f"Перемещённая папка не найдена. Код: {moved_get.status_code}. "
                f"Ответ: {moved_get.text}"
            )
    finally:
        cleanup_response = client.delete_resource(moved_path, permanently=True)
        assert cleanup_response.status_code in (204, 202, 404), (
            f"Не получилось удалить папку после move. Код: {cleanup_response.status_code}. "
            f"Ответ: {cleanup_response.text}"
        )

# Проверка метода DELETE
def test_delete_folder(client, folder_path):
    create_response = client.create_folder(folder_path)
    assert create_response.status_code in (201, 409), (
        f"Папка не создалась перед удалением. Код: {create_response.status_code}. "
        f"Ответ: {create_response.text}"
    )

    delete_response = client.delete_resource(folder_path, permanently=True)
    assert delete_response.status_code in (204, 202), (
        f"Папка не удалилась. Код: {delete_response.status_code}. "
        f"Ответ: {delete_response.text}"
    )

    if delete_response.status_code == 204:
        check_response = client.get_resource(folder_path)
        assert check_response.status_code == 404, (
            f"После удаления папка всё ещё есть. Код: {check_response.status_code}. "
            f"Ответ: {check_response.text}"
        )
