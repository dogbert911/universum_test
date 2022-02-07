from universum.configuration_support import Configuration, Step

configs = Configuration([
  Step('Long success step', command=['./test.sh', 'Text', '100', '1', '0' ]),
  Step('Success stderr', command=['./test.sh', 'Error text', '20', '2', '0' ]),
  Step('Error stderr', command=['./test.sh', 'Error text', '20', '2', '1' ]),
  Step('Error stdout', command=['./test.sh', 'Normal text', '20', '1', '2' ]),
  Step('Critical step', command=['./test.sh', 'Normal text', '20', '1', '2' ], critical=True),
])
