from django.apps import AppConfig

from pone_infra.etherscan.threads.AsyncEthScanThread import AsyncEthScanThread

class EtherscanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pone_infra.etherscan'

    def ready(self) -> None:
        # daemon
        AsyncEthScanThread().start()

        return super().ready()
