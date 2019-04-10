# https://gist.github.com/yoheioka/5222caaaa0f80ad7ddb47d1e3be82e83#file-slack-py
# -*- coding: utf-8 -*-
import json
import requests

class Slack:

    # TODO
    WEBHOOK_URL = (
        'https://hooks.slack.com/services///' # Complete WEBHOOK Address
    )

    def _post_slack_message(self, text):
        slack_data = {
            'text': text,
            'mrkdwn': True
        }

        requests.post(
            self.WEBHOOK_URL,
            data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )

    def send_notification(self, message):
        self._post_slack_message(message)

    def test_notification(self):
        self.send_notification('test message')

if __name__ == '__main__':
    Slack().test_notification()