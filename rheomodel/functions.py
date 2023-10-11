# -*- coding: utf-8 -*-
import bibtexparser
import pandas as pd

library = bibtexparser.parse_file('./rheomodel/models.bib')


def library_to_renderjson(library):
    
    import json
    from IPython.display import display, HTML

    def render_json(data):
        json_str = json.dumps(data, indent=2)
        html = '<div id="json-collapsible" style="height: auto; width:100%;"></div>'
        html += '''<script>
            require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
                renderjson.set_show_to_level(1);
                document.getElementById('json-collapsible').appendChild(renderjson(%s));
            });
        </script>''' % json_str
        display(HTML(html))


    bib_records={}
    for entry in library.entries:
        record_dict={key: value.value for key,value in entry.fields_dict.items()}
        bib_records[entry.key]=record_dict

    return render_json(bib_records)


def library_to_table(library):

    bib_records=[]
    for entry in library.entries:
        record_dict={key: value.value for key,value in entry.fields_dict.items()}
        record_dict['ID']=entry.key
        bib_records.append(record_dict)

    table=pd.DataFrame.from_records(bib_records).set_index('ID')
    return table