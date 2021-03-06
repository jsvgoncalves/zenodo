# -*- coding: utf-8 -*-
#
## This file is part of ZENODO.
## Copyright (C) 2014 CERN.
##
## ZENODO is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## ZENODO is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with ZENODO. If not, see <http://www.gnu.org/licenses/>.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

from __future__ import absolute_import

from fixture import DataSet


class CommunityData(DataSet):
    class zenodo:
        id = 'zenodo'
        title = 'ZENODO'
        id_user = 2
        has_logo = False

    class ecfunded:
        id = 'ecfunded'
        title = 'European Commission Funded Research (OpenAIRE)',
        curation_policy = 'Uploads must have been fully or partially funded ' \
                          'by the European Commission.'
        id_user = 2  # info@zenodo.org
        has_logo = False
