from lib import action


class VaultGetHealthStatusAction(action.VaultBaseAction):
    def run(self):
        return self.vault.sys.read_health_status(method='GET')