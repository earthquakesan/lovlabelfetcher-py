# lovlabelfetcher-py
Python interface for LOV dataset [1].
Fetches the labels for all available terms in LOV.

## How to use
First install lovlabelfetcherpy from the pipy:
```
pip install lovlabelfetcherpy
```

Then you can include it into your application and get coherence for a list of words as follows:
```
from lovlabelfetcherpy.lovlabelfetcher import LOVLabelFetcher
label_fetcher = LOVLabelFetcher()
uri = "http://open.vocab.org/terms/hudYear"
label_fetcher.get_label(uri)
```
In case URI does not exist LOV label fetcher will return you None (see tests).

## Index

The index was built using the following SPARQL query:
```
select distinct ?uri ?label {
  ?uri rdfs:label ?label .
  FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en"))
}
```
You can find index in labels.csv file.

### References
[1] [LOV Project](http://lov.okfn.org/dataset/lov/about)

## Development Setup & Testing
```
  pip install -r requirements.txt
  pip install -e ./
  make test
```

## Contributors

Ivan Ermilov: [my github account](https://github.com/earthquakesan)

## License

This interface is licensed with Apache 2.0 license. For LOV Project license, see [their website](https://lov.okfn.org).
