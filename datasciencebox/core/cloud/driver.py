from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from datasciencebox.core.logger import getLogger
logger = getLogger()


class Driver(object):

    @classmethod
    def new(cls, settings):
        logger.debug('Creating new driver')
        cloud = settings['CLOUD'].lower()
        if cloud == 'bare':
            return None
        elif cloud == 'aws':
            return Driver.aws_create(settings)
        elif cloud == 'gcp':
            return Driver.gcp_create(settings)

    @classmethod
    def aws_create(cls, settings):
        logger.debug('Creating AWS driver')
        cls = get_driver(cls.aws_region_map[settings['AWS_REGION'].lower()])
        return cls(settings['AWS_KEY'], settings['AWS_SECRET'])

    aws_region_map = {
        'us-east-1': Provider.EC2_US_EAST,
        'us-west-1': Provider.EC2_US_WEST,
        'us-west-2': Provider.EC2_US_WEST_OREGON,
        'eu-west-1': Provider.EC2_EU_WEST,
        'eu-central-1': None,
        'sa-east-1': Provider.EC2_SA_EAST,
        'ap-northeast-1': Provider.EC2_AP_NORTHEAST,
        'ap-southeast-1': Provider.EC2_AP_SOUTHEAST,
        'ap-southeast-2': Provider.EC2_AP_SOUTHEAST2,
    }

    @classmethod
    def gcp_create(cls, settings):
        logger.debug('Creating GCP driver')
        import libcloud.security
        libcloud.security.VERIFY_SSL_CERT = False

        ComputeEngine = get_driver(Provider.GCE)
        driver = ComputeEngine(settings['GCP_EMAIL'],
                               settings['GCP_KEY_FILE'],
                               project=settings['GCP_PROJECT'],
                               datacenter=settings['GCP_DATACENTER'])
        return driver
