"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, HttpClient
from .sdkconfiguration import SDKConfiguration, ServerEnvironment
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
import httpx
from t742874298_1 import models, utils
from t742874298_1._hooks import SDKHooks
from t742874298_1.pet_sdk import PetSDK
from t742874298_1.store import Store
from t742874298_1.types import OptionalNullable, UNSET
from t742874298_1.user_sdk import UserSDK
from typing import Any, Callable, Dict, List, Optional, Union


class Petstore(BaseSDK):
    r"""Petstore - OpenAPI 3.1: This is a sample Pet Store Server based on the OpenAPI 3.1 specification.

    Some useful links:
    - [OpenAPI Reference](https://www.speakeasy.com/openapi)
    - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)
    - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)
    http://swagger.io - Find out more about Swagger
    """

    pet: PetSDK
    r"""Everything about your Pets
    http://swagger.io - Find out more
    """
    store: Store
    r"""Access to Petstore orders
    http://swagger.io - Find out more about our store
    """
    user: UserSDK
    r"""Operations about user"""

    def __init__(
        self,
        api_key: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        environment: Optional[ServerEnvironment] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :param environment: Allows setting the environment variable for url substitution
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(api_key):
            security = lambda: models.Security(api_key=api_key())  # pylint: disable=unnecessary-lambda-assignment
        else:
            security = models.Security(api_key=api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults: List[Dict[str, str]] = [
            {
                "environment": environment or "prod",
            },
        ]

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                server_defaults=server_defaults,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        self._init_sdks()

    def _init_sdks(self):
        self.pet = PetSDK(self.sdk_configuration)
        self.store = Store(self.sdk_configuration)
        self.user = UserSDK(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()
