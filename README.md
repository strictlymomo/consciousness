# consciousness

Exploring Consciousness.
This project will collect and analyze youtube transcripts on the topics of consciousness to create a map of the ideas and theories that are being discussed.

**Channels**

- [Theories of Everything with Curt Jaimungal](https://www.youtube.com/TheoriesOfEverything)
- [Closer To Truth](https://www.youtube.com/@CloserToTruthTV)
- [New Thinking Allowed with Jeffrey Mishlove](https://www.youtube.com/@NewThinkingAllowed)

## Workflow

0. Provision environment and dependencies

   - `sh init.sh`

1. Get data programmatically from [youtube](https://developers.google.com/youtube/v3/getting-started)

   - `sh hello-world.sh`

2. Extract transcripts

   - See `python3 -m hello-world"`
   - Format txt files:
     - Readability
     - remove line breaks
     - break lines into paragraphs
     - convert paragraphs into single lines
     - Timestamps (dunno how to map via json)
     - Speaker (dunno how to map via json)

3. Analyze transcripts

   - See `hello-world.ipynb`
