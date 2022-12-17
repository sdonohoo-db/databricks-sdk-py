# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateCredentials:

    # Git provider. This field is case-insensitive. The available Git providers are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str
    # The personal access token used to authenticate to the corresponding Git provider.
    personal_access_token: str

    def as_dict(self) -> dict:
        body = {}
        if self.git_provider:
            body["git_provider"] = self.git_provider
        if self.git_username:
            body["git_username"] = self.git_username
        if self.personal_access_token:
            body["personal_access_token"] = self.personal_access_token

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCredentials":
        return cls(
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
            personal_access_token=d.get("personal_access_token", None),
        )


@dataclass
class CreateCredentialsResponse:

    # ID of the credential object in the workspace.
    credential_id: int
    # Git provider. This field is case-insensitive. The available Git providers are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id:
            body["credential_id"] = self.credential_id
        if self.git_provider:
            body["git_provider"] = self.git_provider
        if self.git_username:
            body["git_username"] = self.git_username

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateCredentialsResponse":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
        )


@dataclass
class CredentialInfo:

    # ID of the credential object in the workspace.
    credential_id: int
    # Git provider. This field is case-insensitive. The available Git providers are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id:
            body["credential_id"] = self.credential_id
        if self.git_provider:
            body["git_provider"] = self.git_provider
        if self.git_username:
            body["git_username"] = self.git_username

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CredentialInfo":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
        )


@dataclass
class Delete:
    """Delete a credential"""

    # The ID for the corresponding credential to access.
    credential_id: int  # path


@dataclass
class Get:
    """Get a credential entry"""

    # The ID for the corresponding credential to access.
    credential_id: int  # path


@dataclass
class GetCredentialsResponse:

    credentials: "List[CredentialInfo]"

    def as_dict(self) -> dict:
        body = {}
        if self.credentials:
            body["credentials"] = [v.as_dict() for v in self.credentials]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GetCredentialsResponse":
        return cls(
            credentials=[CredentialInfo.from_dict(v) for v in d["credentials"]]
            if "credentials" in d
            else None,
        )


@dataclass
class UpdateCredentials:

    # The ID for the corresponding credential to access.
    credential_id: int  # path
    # Git provider. This field is case-insensitive. The available Git providers are awsCodeCommit, azureDevOpsServices,
    git_provider: str
    # Git username.
    git_username: str
    # The personal access token used to authenticate to the corresponding Git provider.
    personal_access_token: str

    def as_dict(self) -> dict:
        body = {}
        if self.credential_id:
            body["credential_id"] = self.credential_id
        if self.git_provider:
            body["git_provider"] = self.git_provider
        if self.git_username:
            body["git_username"] = self.git_username
        if self.personal_access_token:
            body["personal_access_token"] = self.personal_access_token

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "UpdateCredentials":
        return cls(
            credential_id=d.get("credential_id", None),
            git_provider=d.get("git_provider", None),
            git_username=d.get("git_username", None),
            personal_access_token=d.get("personal_access_token", None),
        )


class GitCredentialsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        git_provider: str,
        *,
        git_username: str = None,
        personal_access_token: str = None,
        **kwargs,
    ) -> CreateCredentialsResponse:
        """Create a credential entry.

        Creates a Git credential entry for the user. Only one Git credential per
        user is supported, so any attempts to create credentials if an entry
        already exists will fail. Use the PATCH endpoint to update existing
        credentials, or the DELETE endpoint to delete existing credentials."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = CreateCredentials(
                git_provider=git_provider,
                git_username=git_username,
                personal_access_token=personal_access_token,
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/git-credentials", body=body)
        return CreateCredentialsResponse.from_dict(json)

    def delete(self, credential_id: int, **kwargs):
        """Delete a credential.

        Deletes the specified Git credential."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Delete(credential_id=credential_id)

        self._api.do("DELETE", f"/api/2.0/git-credentials/{request.credential_id}")

    def get(self, credential_id: int, **kwargs) -> CredentialInfo:
        """Get a credential entry.

        Gets the Git credential with the specified credential ID."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Get(credential_id=credential_id)

        json = self._api.do("GET", f"/api/2.0/git-credentials/{request.credential_id}")
        return CredentialInfo.from_dict(json)

    def list(self) -> GetCredentialsResponse:
        """Get Git credentials.

        Lists the calling user's Git credentials. One credential per user is
        supported."""

        json = self._api.do("GET", "/api/2.0/git-credentials")
        return GetCredentialsResponse.from_dict(json)

    def update(
        self,
        credential_id: int,
        *,
        git_provider: str = None,
        git_username: str = None,
        personal_access_token: str = None,
        **kwargs,
    ):
        """Update a credential.

        Updates the specified Git credential."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = UpdateCredentials(
                credential_id=credential_id,
                git_provider=git_provider,
                git_username=git_username,
                personal_access_token=personal_access_token,
            )
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/git-credentials/{request.credential_id}", body=body
        )