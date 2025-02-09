# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXml(RPackage):
    """Tools for Parsing and Generating XML Within R and S-Plus.

    Many approaches for both reading and creating XML (and HTML) documents
    (including DTDs), both local and accessible via HTTP or FTP. Also offers
    access to an 'XPath' "interpreter"."""

    cran = "XML"

    version('3.99-0.9', sha256='9c15dedf3157efc59e0db31506631dfe770a4d397ce52f972434bed60e206a09')
    version('3.99-0.8', sha256='081f691c2ee8ad39c7c95281e7d9153ec04cee79ca2d41f5d82c2ec2f1d36b50')
    version('3.99-0.5', sha256='60529b7360f162eba07da455eeb9b94a732b2dd623c49e0f04328a2e97bd53a6')
    version('3.98-1.20', sha256='46af86376ea9a0fb1b440cf0acdf9b89178686a05c4b77728fcff1f023aa4858')
    version('3.98-1.19', sha256='81b1c4a2df24c5747fa8b8ec2d76b4e9c3649b56ca94f6c93fbd106c8a72beab')
    version('3.98-1.9', sha256='a3b70169cb2fbd8d61a41ff222d27922829864807e9ecad373f55ba0df6cf3c3')
    version('3.98-1.5', sha256='deaff082e4d37931d2dabea3a60c3d6916d565821043b22b3f9522ebf3918d35')
    version('3.98-1.4', sha256='9c0abc75312f66aac564266b6b79222259c678aedee9fc347462978354f11126')

    depends_on('r@2.13.0:', type=('build', 'run'))
    depends_on('r@4.0.0:', type=('build', 'run'), when='@3.99-0.5:')
    depends_on('libxml2@2.6.3:')
