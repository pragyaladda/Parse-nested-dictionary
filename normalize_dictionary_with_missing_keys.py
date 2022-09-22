list_ = [
    {'Name': 'Paras Jain',
  'Student': [{'Exam': 90,
               'remark': ['hari: PASS', 'meena: FAIL', 'rajesh: FAIL'],
               'class': [{'age': 10},
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
 {'Name': 'Chunky Pandey'}
]

class Solution:

    def _recursive_parse_data(self, val, dict_, out, final_dict, key=None):
        if isinstance(val, str):
            dict_[key] = val
        count = 0
        if isinstance(val, list):
            for rec in val:
                if count > 0:
                    if dict_ not in out:
                        [dict_.update({i: ''}) for i in final_dict.keys() if not dict_.get(i)]
                        out.append(dict_)
                    if key:
                        dict_ = {k:v for k,v in dict_.items() if key not in k}
                    else:
                        dict_ = {}
                self._recursive_parse_data(rec, dict_, out, final_dict, key)
                count += 1
            if dict_ not in out:
                [dict_.update({i: ''}) for i in final_dict.keys() if not dict_.get(i)]
                out.append(dict_)
        if isinstance(val, dict):
            for i in val.keys():
                if key:
                    key_i = key+"_"+i
                else:
                    key_i = i
                if val[i] and isinstance(val[i], list) and isinstance(val[i][0], dict):
                    self._recursive_parse_data(val[i], dict_, out, final_dict, key=key_i)
                else:
                    if val[i] and isinstance(val[i], list):
                        data = '\n'.join(i for i in val[i] if not i.endswith("PASS"))
                    else:
                        data = val[i]
                    self._recursive_parse_data(str(data), dict_, out, final_dict, key=key_i)


    def parseData(self, res):
        out = []
        final_dict = {
            'Name': '',
            'Student_Exam': '',
            'Student_Grade': '',
            'Student_remark': '',
            'Student_class_age': '',
            'Student_class_subject': ''
        }
        self._recursive_parse_data(res, {}, out, final_dict)
        print(out)


if __name__=="__main__":
    sol = Solution()
    sol.parseData(list_)
