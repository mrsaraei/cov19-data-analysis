from setuptools import setup

setup(
    name='covidseverity',
    version='0.1.0',
    description='The COVID-19 Severity Score Using CSV Data',
    author='Mohammadreza Saraei',
    author_email='mrsaraei3@gmail.com',
    url='https://github.com/mrsaraei/Covid19_Data_Analysis/covidseverity',
    packages=['covidseverity'],
    install_requires=['numpy', 'pandas', 'matplotlib', 'scikit-plot', 'scikit-learn'],
    license='MIT License',
)
