# -*- coding: utf-8 -*-
# @Author: shisan-yan
# @Date:   2017-12-07 14:54:45
# @Last Modified by:   shisan-yan
# @Last Modified time: 2017-12-07 14:56:27

def createNum():
	print '-------start--------'

	a,b = 0,1

	for i in range(5):
		print '-------1--------'
		yield b
		print '-------2--------'
		a,b = b,a+b
		print '-------3---------'
	print '-------stop-----------'


