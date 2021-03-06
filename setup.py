from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='claudinha_text',
      version='1.0',
      description='Create ASCII scrolling text in Raspberry PI \
        with Unicorn Hat',
      url='https://github.com/claudinha-io/claudinha-module',
      author='Camilla Gomes',
      author_email='lobinhaxd@gmail.com',
      license='MIT',
      packages=['claudinha_text'],
      package_data={
        '': ['*.json']
      },
      install_requires=reqs,
      zip_safe=False)
