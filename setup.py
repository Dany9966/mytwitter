from setuptools import setup

setup(
    pbr=True,
    name="mytwitter",
    version="0.0.1",
    author="Lucian Petrut",
    description="""
Sample app showing a few concepts such as rpc via amqp,
sqlalchemy, logging, simple config parsing, argument parsing.
""",
    packages=['mytwitter'],
    install_requires=['pika', 'sqlalchemy'],
    entry_points={
        'console_scripts': [
            'mytwitter_client = mytwitter.cmd.client:main',
            'mytwitter_server = mytwitter.cmd.server:main',
            'mytwitter_api = mytwitter.cmd.api:main'
        ],
    }
)
