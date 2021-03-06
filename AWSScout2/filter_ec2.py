#!/usr/bin/env python2

from AWSScout2.filter import *


class Ec2Filter(Filter):

    def __init__(self, description, entity, callback, callback_args):
        self.keyword_prefix = 'ec2'
        Filter.__init__(self, description, entity, callback, callback_args)

    def hasNoRunningInstances(self, key, obj):
        if len(obj['running-instances']) == 0:
            self.addItem(obj['id'])

    def HasNoCIDRsGrants(self, key, obj):
        if not len(obj['protocols']):
            self.addItem(obj['id'])
            return
        for protocol in obj['protocols']:
            for rule in obj['protocols'][protocol]['rules']:
                if not 'cidrs' in rule['grants']:
                    self.addItem(obj['id'])

    def DoesNotOpenAllPorts(self, key, obj):
        if not len(obj['protocols']):
            self.addItem(obj['id']);
            return
        for protocol in obj['protocols']:
            for rule in obj['protocols'][protocol]['rules']:
                if rule['ports'] != '1-65535' and rule['ports'] != 'All':
                    self.addItem(obj['id'])
