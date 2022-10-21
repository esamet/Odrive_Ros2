from setuptools import setup

package_name = 'rover_info'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samet',
    maintainer_email='samete354@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battvoltage = rover_info.battvoltage:main','tempinfo = rover_info.tempinfo:main','robotcmdvel = rover_info.robotcmdvel:main','robot_odom = rover_info.robot_odom:main'
        ],
    },
)
