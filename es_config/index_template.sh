# Index template to specify number of shards and number of replicas
curl -XPUT -u es-atlas 'https://es-atlas.cern.ch:9203/_template/template_atlas_pandalogs' -d '
{
    "template" : "atlas_pandalogs*",
    "settings" : {
        "number_of_shards" : 20,
        "number_of_replicas" : 1
    }
}
'