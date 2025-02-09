from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'gps_waypoint_nav'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='raza',
    maintainer_email='smrazarizvi96@gmail.com',
    description='ROS2 package for GPS Waypoint navigation with velocity commands',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_waypoint_nav = gps_waypoint_nav.gps_waypoint_nav:main',
        ],
    },
)
