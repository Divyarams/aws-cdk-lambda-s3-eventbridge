#!/usr/bin/env python3
import os

import aws_cdk as cdk

from eventlistener.eventlistener_stack import EventlistenerStack


app = cdk.App()
EventlistenerStack(app, "EventlistenerStack")

app.synth()
