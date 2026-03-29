# tests/test_auth.py


def test_signup_success(client):
    response = client.post(
        "/api/auth/signup",
        json={"email": "test@example.com", "password": "securepassword123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_signup_duplicate_email(client):
    # 1. Create the first user
    client.post(
        "/api/auth/signup", json={"email": "clone@example.com", "password": "pass"}
    )

    # 2. Try to create the exact same user
    response = client.post(
        "/api/auth/signup", json={"email": "clone@example.com", "password": "pass"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"


def test_signin_success_and_cookie(client):
    # Setup: Ensure user exists
    client.post(
        "/api/auth/signup", json={"email": "login@example.com", "password": "pass"}
    )

    # Action: Sign in
    response = client.post(
        "/api/auth/signin", json={"email": "login@example.com", "password": "pass"}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Successfully logged in"}

    # Verify the HttpOnly cookie was actually attached to the response
    assert "access_token" in response.cookies


def test_get_me_unauthorized(client):
    # Action: Try to access protected route without logging in
    response = client.get("/api/me")
    assert response.status_code == 401


def test_get_me_authorized(client):
    # Setup: Create user and login
    client.post(
        "/api/auth/signup", json={"email": "alfialdo@example.com", "password": "pass"}
    )
    login_res = client.post(
        "/api/auth/signin", json={"email": "alfialdo@example.com", "password": "pass"}
    )

    # Extract the cookie the server sent back
    token = login_res.cookies.get("access_token")

    # Action: Request the protected route, explicitly passing the cookie
    response = client.get("/api/me", cookies={"access_token": token})

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome, alfialdo"}


def test_signout(client):
    response = client.post("/api/auth/signout")
    assert response.status_code == 200

    # Verify the server told the browser to delete the cookie (max-age=0 or expires)
    cookie_header = response.headers.get("set-cookie", "")
    assert "access_token=" in cookie_header
    assert "Max-Age=0" in cookie_header or "expires=" in cookie_header.lower()
