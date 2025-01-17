import configs
import torch


class Run(configs.BaseConfig):

    def __init__(self, cfg):
        super(Run, self).__init__(cfg)
        self._more()

    def _more(self):
        self.cuda = torch.cuda.is_available() and getattr(self, 'cuda', True)
        torch.backends.cudnn.benchmark = self.cuda

    @staticmethod
    def all():
        return configs.all(Run, configs.env.getdir(configs.env.paths.run_cfgs_folder))


if __name__ == "__main__":
    print(Run.all())
