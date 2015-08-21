try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='emoji-ipython-magic',
    version='0.0.1',
    author="Austin Rochford",
    author_email="austin.rochford@gmail.com",
    description="emoji magic for IPython 3",
    install_requires=['ipython<=3.2.1', 'emoji'],
    keywords="ipython",
    license="MIT",
    long_description="""This package provides a line magic for rendering emoji in an IPython notebook""",
    platforms='any',
    py_modules=['emoji_magic'],
    url="https://github.com/AustinRochford/emoji-ipython-magic",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
