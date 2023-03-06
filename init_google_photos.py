import pandas as pd

import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.http import MediaFileUpload

from Google import Create_Service


def get_album_df(service):
    """
    Returns a list of Albums in the Account
    """

    response = service.albums().list().execute()
    album_names = [album["title"] for album in response["albums"]]
    albums = response["albums"]
    print(response.keys())

    nextPageToken = None
    if "nextPageToken" in response:
        nextPageToken = response["nextPageToken"]

    count = 0  # circuit-breaker
    while "nextPageToken" in response and count < 10:
        nextPageToken = response["nextPageToken"]
        response = service.albums().list(pageToken=nextPageToken).execute()
        album_names = [album["title"] for album in response["albums"]]
        print(response.keys())
        print(f"Albums Length {len(response['albums'])}")
        print()
        albums += response["albums"]
        if "nextPageToken" in response:
            nextPageToken = response["nextPageToken"]
        count += 1

    print(len(albums), type(albums))
    df_albums = pd.DataFrame(albums)
    # print(df_albums.head())
    return df_albums


if __name__ == "__main__":

    API_NAME = "photoslibrary"
    API_VERSION = "v1"

    CLIENT_SECRET_FILE = "data/client_secret_df-life_2023-03-01.json"
    # Define the scopes that will be authorized for the credentials
    SCOPES = [
        "https://www.googleapis.com/auth/photoslibrary",
        "https://www.googleapis.com/auth/photoslibrary.sharing",
    ]
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    df = get_album_df(service)
    print(df.columns)
    useful_columns = ["title", "productUrl", "mediaItemsCount"]
    print(df[useful_columns])

