from django.apps import AppConfig

from one_infra.etherscan.threads.AsyncEthScanThread import AsyncEthScanThread

class EtherscanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'one_infra.etherscan'

    def ready(self) -> None:
        # daemon
        AsyncEthScanThread().start()

        return super().ready()
