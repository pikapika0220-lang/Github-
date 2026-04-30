def change_domain(email, domain):
    return '@'.join([email.split('@')[0],domain])
print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')