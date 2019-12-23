# Project description

Expected user input: transfer function (TF) of LTI system in Laplace (so called S-) domain
	-User is asked to enter highest order term in numerator and denominator of transfer function
		(if order of numerator is greater than order of denominator, transfer function is not valid)
	-After that, user is asked to enter coefficents firstly for the numerator, where first entered coeff.
	is related to highest term of TF, second coeff. to second term, etc.)
		-If entered coefficent for highest order term is 0 - error
	-Same for the denominator

Steps:
		1.Based on the transfer function in S-domain, system stability can be obtained using criterion for poles 
		2.Replacing s with jw, where j is complex number, we get frequency characteristic of given system
			2.1.Amplitude vs frequency then can be easily calculated as absolute value of system's frequency characteristic
			2.2.Phase vs frequency as arc tan of f.c.
			