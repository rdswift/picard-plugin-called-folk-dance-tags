# Called Folk Dance Tags

This plugin adds tags for traditional called folk dances from the IETF Internet-Draft (I-D) [draft-swhited-contra-tags-04](https://datatracker.ietf.org/doc/draft-swhited-contra-tags/). It is based on a pull request by Sam Whited to include the tags in the Picard base code.

The plugin creates the tags, with descriptions, for easy lookup in the script editor only. It does not populate any of the tags. Tags include:

- `dance_caller`: The name of the dance caller(s) heard in the track.
- `dance_choreographer`: The names of the authors of the dances being called.
- `dance_choreography`: The moves of the dance as text for called folk dances.
- `dance_crooked`: Whether a traditional called folk dance tune is "crooked" (ie. not in perfect dance form).
- `dance_form`: The form of a called dance with no particular format, eg. "contra" or "square dance" or "duple minor improper contra".
- `dance_intro`: The number of intro beats before the dance or any potatoes for called folk dances.
- `dance_issong`: Whether the track is a song (has sung vocals other than the caller) or a tune (instrumental only) for traditional music forms that make this distinction.
- `dance_license`: Like the license field except relating to the choreography of the dance being called for called folk dances.
- `dance_potatoes`: The number of "potatoes" (syncronization beats played before some traditional folk dances).
- `dance_roles`: The role terms used for calls in a called folk dance, eg. "Larks/Robins" or "Leads/Follows" or "Positional".
- `dance_start`: The start time (in milliseconds) of the first time through the dance in a called folk dance.
- `dance_times`: The number of complete times through the dance excluding any intro, outro, or potatoes for a called folk dance. The exact definition will depend on the type of dance.
- `dance_title`: The name of the dance(es) being called for called folk dances.

## Contributing

Please see the [Contribution Guidelines for MusicBrainz Picard Plugins](https://github.com/metabrainz/picard-plugins-registry/blob/main/PLUGIN_CONTRIBUTING.md) on how to help with development of this plugin.
