# Python Price Researcher (*pryce*)

> *PRYCE: When every penny counts!*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This project was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

The idea for this project came from reading Maciej Janowski's [How to develop extensible web scraper with Python, requests and bs4](https://janowski.dev/blog/how-develop-extensible-web-scraper-python-requests-and-bs4/) tutorial.
 
## Initial setup

```zsh
cd Projects
git clone https://github.com/clamytoe/pryce.git
cd pryce
```

### Anaconda setup

If you are an Anaconda user, this command will get you up to speed with the base installation.

```zsh
conda env create
conda activate pryce
```

### Regular Python setup

If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment. There are many ways to do this, the simplest using *venv*.

```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Final setup

```zsh
pip install -e .
```

## Usage

It's simple to use, you just enter the command `pryce` and it will prompt you to enter what you are looking for.
Once you hit enter, it will search for what you entered on eBay and also Barnes and Noble and store the results in CSV files.
```zsh
pryce
search term: python book
20 items saved to barnesandnoble_2020-04-26.csv
63 items saved to ebay_2020-04-26.csv
```

The output will have the following entries: `url`, `image url`, `name`, `price`

Here's a sample from each:

#### Barnes and Noble

```csv
url,image,name,price
https://www.barnesandnoble.com/w/python-crash-course-2nd-edition-eric-matthes/1129705311;jsessionid=F19311912916C233542E128640FD147B.prodny_store01-atgap16?ean=9781593279288,https://prodimage.images-bn.com/pimages/9781593279288_p0_v2_s192x300.jpg,"Python Crash Course, 2nd Edition",$35.95
https://www.barnesandnoble.com/w/python-all-in-one-for-dummies-john-shovic/1129527136;jsessionid=F19311912916C233542E128640FD147B.prodny_store01-atgap16?ean=9781119557593,https://prodimage.images-bn.com/pimages/9781119557593_p0_v4_s192x300.jpg,Python All-in-One For Dummies,$35.99
```

#### eBay

```csv
url,image,name,price
https://www.ebay.com/itm/Learning-Python-5th-Edition-by-Mark-Lutz-P-D-F-Digital/373024691674?epid=159818827&_trkparms=ispr%3D1&hash=item56da0115da:g:Sx0AAOSwPPlemkU0&enc=AQAEAAACYIQvEcHUrT7nmUC3yY5qbPyaBN1nJEDYW8MyypsJPgXKQAYcH4BGwQtpYi1R8mhqgKeVRVjBT8y7ZWb89fDOpryWUgf0THIADujLfdreTjNdxdDL7Ho9hGlrunzP%2FeO%2BjPqo1cA1YMZrjVldYGi4PigGwAaDlna2HGx2AkOUvdkjVrXRSG9uUQJ4EAHfQk5Yzug1V7DC4NkgqfItgz0uPmjZKPLTU%2BJRIhf%2Bgu%2B76ie0uOyxgz8uHoVfGBbIIAR1bsQJsYzhaLFSZS8Z5f9ZLXznXbLa%2Fn5WPd0WmvYk3JbjdShaG3UNhnYOf%2FB73e1yX4gr4bl3BpRi412ON4C2epgKk264qdOGGTBxPZC6HwuNWH8lqeR%2BCLdNcaU9TJzQCC5NeCRPDXIxpYT19wb3JRuA9ynQZzqUBkbedyQFifKCzSYDCA41cGRiuZ0InUu3dpOVOGl8nh9L9CRdOvhHGw%2BS5Ft%2FY8xZDXz4b5ugvk7bUWkc%2Bl9PPGN%2BTxEgL7uyecu4kYUfroH6Da1buliXFa0JSy6Q05oHsAFMjBPinZlK1kQWHSE3P2ZAVfOWLBt9%2FBHUlV8nxQFMabMlPQRR6bQFXp86TFfd%2B65KBRg9zTo4drXU09o83rxW0FMp5wwKxLuX%2BGDldg8FqVLlkIBKneyQ1yXzKql%2B9egMhQy3GBbuDurKoBkrWae1Zs7pVI8byDs7ot9%2BVJZNpkUhs%2Bwy9nbEjiHYYbZdK4G%2Bmy8EipuUGCd%2FF6A4GaP7ZjBUO0m9LIrmmEFWGP8Njm1XFqMH0G%2F2DRBiof4zaN2jra5nOsI7&checksum=373024691674eec3b117d27745aeb8437c38a7402cf0,https://i.ebayimg.com/thumbs/images/g/Sx0AAOSwPPlemkU0/s-l225.jpg,"Learning Python, 5th Edition by Mark Lutz [P.D.F] Digital",$4.99
https://www.ebay.com/itm/Learning-Python-5th-Edition-by-Mark-Lutz-P-D-F/353041007998?epid=159818827&_trkparms=ispr%3D1&hash=item5232e2457e:g:uiAAAOSwHy5ejb3N&enc=AQAEAAACYIQvEcHUrT7nmUC3yY5qbPyaBN1nJEDYW8MyypsJPgXKVSUO5rLpLbvuHeymugu80jkeJwMVfeCKeg0ITkgGVQMkBeUPcbS8Byu%2BB13VFMdGVgU0Hs6FKIp3IYpat7zZ32icqQ7u30uazZOD3tLhEluvmSlxCs31UcMmL0sxZpF9rFEMyXDTZi%2FqsQGBjCnwJ2z97oLYXie4redXB6D%2BMAoZVbUvwRCAFvo6qZJasT8td5ezlWbSFRPrqCYU81GoswQWDF%2BPYm6F3NWf3UiZRC7kp%2FNPZF1BWRFzF1s%2FpKShfi62vMwBiWGjwDG14Y%2BE6u3FXFSvgvNh599vc8Cn3z%2F6rxepMaQ9twe1xu5%2FCcQhhq8RF9y5nSx%2FsL2Uc79cVWzBm66RF%2BD44iRczHpCgINOR0BVhnh8Wm73DnJ56gIU7IYvBOE3t%2BZKGs5IvaHNwRoWz0cW9%2BdHKB9Q4mO7a4BVgYkI2hauzB7g%2BAJ7V7LBRvJTaFE7NxeEXiViIbs%2FGbRa6TN7RzSGUNHE2mxT5%2Fj4OFMxalFF0MDe%2BhVpAuS%2BorlvZq6ZAydpX98e8iMMfW9SoqQZqs%2BHru1NE2MAW9%2FY9XhJVYo5b%2FjhiEV36KNxZ3iCGWA4nae0ICq4M0SBx6U3Q4PC240YGEtb6KyobSVxH%2FfpiAUjwQjmKrUm2FA1OmlH%2FdbPS9c4i1XV0V4oqyUpdWSK%2FeAjWt23FSCgKNh8Cp%2BfsHd2Vik3nmfacVog1CABO2v%2BKGPQ%2B55heBAf%2FXk7iEBEPZt068%2BIkEeiof1Ex55bXGdX7DwU3VBHW8FM&checksum=353041007998eec3b117d27745aeb8437c38a7402cf0,https://i.ebayimg.com/thumbs/images/g/uiAAAOSwHy5ejb3N/s-l225.jpg,"Learning Python, 5th Edition by Mark Lutz [P.D.F]",$5.46
https://www.ebay.com/itm/Python-for-Data-Analysis-Digital-Book/164017149155?_trkparms=ispr%3D1&hash=item26302f14e3:g:CWQAAOSwRfNeJajb&enc=AQAEAAACYIQvEcHUrT7nmUC3yY5qbPyaBN1nJEDYW8MyypsJPgXKym2Jdff8P6pcVkPslsrmD%2FKB5Tt5obK4SAXz8AMh7rk%2Bjqb8w3homSNe2yU4pIFSqcTS3Mm%2F7T9gADUVMsf5gNhtXIUv58qU21SyBcj14tQRxv2dBqxNVtnkxCw3dShWz5fgfIOfa01raIg3WdvCbVCWaOjqF3ZNbHjSq03pPqGJxgc574IqF0iP3AFullA9RJsDKgtOmLKerhPr7q%2FDQ%2B0bFYKWuE1IGPHt1RKcW869wCpQnJvgMJdJg5weGRqRSxhZB4j9poYQVYstD5fx8O9MB%2Fjivc1t8SM6CzqVh7evWUqwslZF7WcIZ%2FwgWWpsuA5%2BYP4WidEypGgLLh6Qj5VVz9E8xe1fx6EObVTvp3tmJXx2p4RouYABOlAf1e0u1fUG0FlhdnITn9w0twnCAhJE57N6ggr3nYZL7qjipejotQLwSMM%2BcXq%2BHgI4gnkMedmZ0lsZDXhzMtGRWmMdqX%2BIw0wR8I%2BYYrLHc5Q2I7SBDy6dwoW9rdLJ1sBeIY8eDeTSEAJmYWuxmEGPAzil3yZ7SktRnoolA%2BhQBb7WDiVV14zjG2%2Byi29%2FH5%2BfTuqOSfoBd7kzbI%2BtZMvVsnPGLWQmAdVzCxDNLVWyxx1vGq4Ivv14BOXXaPT%2Byew0EDuKDBFbTo8SLqOHzlklSCbT%2FF5uHCSru46ZmIZF5A4WKDHvKUXNCzB5jBgtYinDP53j0nLV%2FnoKiEpyy25jxPSbbGv%2FlLoQnSWU9sOYdsLOkkjRso3troxyC8kYeaEq6ffY&checksum=164017149155eec3b117d27745aeb8437c38a7402cf0,https://i.ebayimg.com/thumbs/images/g/CWQAAOSwRfNeJajb/s-l225.jpg,Python for Data Analysis - Digital Book -,$5.00
```

## Contributing

Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:

* black
* flake8
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pryce" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.8-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.1.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/pryce.svg
[issues-url]:https://github.com/clamytoe/pryce/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/pryce.svg
[fork-url]:https://github.com/clamytoe/pryce/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/pryce.svg
[stars-url]:https://github.com/clamytoe/pryce/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/pryce.svg
[license-url]:https://github.com/clamytoe/pryce/blob/master/LICENSE
