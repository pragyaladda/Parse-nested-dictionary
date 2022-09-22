list_ = [
    {'Name': 'Paras Jain',
  'Student': [{'Exam': 90,
               'Grade': 'a',
               'remark': ['hari: PASS', 'meena: FAIL', 'rajesh: FAIL'],
               'class': [{'age': 10, 'subject': 'hindi'},
                         {'age': 11, 'subject': 'maths'}]},
              {'Exam': 99,
               'Grade': 'b',
               'remark': ['bob: PASS', 'peter: PASS'],
               'class': [{'age': 14, 'subject': 'evs'},
                         {'age': 15, 'subject': 'science'}]},
              {'Exam': 97,
               'Grade': 'c',
               'remark': [],
               'class': [{'age': 10, 'subject': 'history'}]}]},
 {'Name': 'Chunky Pandey',
  'Student': [{'Exam': 89,
               'Grade': 'a',
               'remark': ['praveen: FAIL'],
               'class': [{'age': 9, 'subject': 'no'}, {'age': 10, 'subject':'no'}]},
              {'Exam': 80, 'Grade': 'b', 'remark': [] ,'class': []}]},
]

class Solution:

    def _recursive_parse_data(self, val, dict_, out, key=None):
        if isinstance(val, str):
            dict_[key] = val
        count = 0
        if isinstance(val, list):
            for rec in val:
                if count > 0:
                    if dict_ not in out:
                        out.append(dict_)
                    if key:
                        dict_ = {k:v for k,v in dict_.items() if key not in k}
                    else:
                        dict_ = {}
                self._recursive_parse_data(rec, dict_, out, key)
                count += 1
            if dict_ not in out:
                out.append(dict_)
        if isinstance(val, dict):
            for i in val.keys():
                if key:
                    key_i = key+"_"+i
                else:
                    key_i = i
                if val[i] and isinstance(val[i], list) and isinstance(val[i][0], dict):
                    self._recursive_parse_data(val[i], dict_, out, key=key_i)
                else:
                    self._recursive_parse_data(str(val[i]), dict_, out, key=key_i)


    def parseData(self, res):
        out = []
        self._recursive_parse_data(res, {}, out)
        print(out)


if __name__=="__main__":
    sol = Solution()
    sol.parseData(list_)
    

