"""Called Folk Dance Tags"""

# Copyright (C) 2026 Bob Swift (rdswift)
# Copyright (C) 2026 Sam Whited (SamWhited)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <https://www.gnu.org/licenses/>.


from picard.plugin3.api import PluginApi


def enable(api: PluginApi) -> None:
    """Called when the plugin is enabled.

    Use api to register plugin hooks and access essential Picard APIs.
    """

    # Scripting variables
    api.register_script_variable(
        name="dance_caller",
        documentation=api.tr(
            "variable.dance_caller",
            "The names of the dance callers heard in the track for called folk dances."
        ),
        title=api.tr("variable.title.dance_caller", "Caller"),
    )

    api.register_script_variable(
        name="dance_choreographer",
        documentation=api.tr(
            "variable.dance_choreographer",
            "The namee of the authors of the dances being called in the track for called folk dances."
        ),
        title=api.tr("variable.title.dance_choreographer", "Dance Choreographer"),
    )

    api.register_script_variable(
        name="dance_choreography",
        documentation=api.tr(
            "variable.dance_choreography",
            (
                "The moves of the dance as text for called folk dances. This should not include the dance title, "
                "author, or other information covered by other tags."
            )
        ),
        title=api.tr("variable.title.dance_choreography", "Dance Choreography"),
    )

    api.register_script_variable(
        name="dance_crooked",
        documentation=api.tr(
            "variable.dance_crooked",
            'Whether a traditional called folk dance tune is "crooked" (ie. not in perfect dance form).'
        ),
        title=api.tr("variable.title.dance_crooked", "Crooked"),
    )

    api.register_script_variable(
        name="dance_form",
        documentation=api.tr(
            "variable.dance_form",
            'The form of a called dance with no particular format, eg. "contra" or "square dance" or "duple minor improper contra".'
        ),
        title=api.tr("variable.title.dance_form", "Dance Form"),
    )

    api.register_script_variable(
        name="dance_intro",
        documentation=api.tr(
            "variable.dance_intro",
            "The number of intro beats before the dance or any potatoes for called folk dances."
        ),
        title=api.tr("variable.title.dance_intro", "Intro Beats"),
    )

    api.register_script_variable(
        name="dance_issong",
        documentation=api.tr(
            "variable.dance_issong",
            (
                "Whether the track is a song (has sung vocals other than the caller) or a tune (instrumental only) for traditional "
                "music forms that make this distinction."
            )
        ),
        title=api.tr("variable.title.dance_issong", "Has Vocals"),
    )

    api.register_script_variable(
        name="dance_license",
        documentation=api.tr(
            "variable.dance_license",
            "Like the license field except relating to the choreography of the dance being called for called folk dances."
        ),
        title=api.tr("variable.title.dance_license", "Dance License"),
    )

    api.register_script_variable(
        name="dance_potatoes",
        documentation=api.tr(
            "variable.dance_potatoes",
            'The number of "potatoes" (syncronization beats played before some traditional folk dances).'
        ),
        title=api.tr("variable.title.dance_potatoes", "Potatoes"),
    )

    api.register_script_variable(
        name="dance_roles",
        documentation=api.tr(
            "variable.dance_roles",
            'The role terms used for calls in a called folk dance, eg. "Larks/Robins" or "Leads/Follows" or "Positional".'
        ),
        title=api.tr("variable.title.dance_roles", "Dance Roles"),
    )

    api.register_script_variable(
        name="dance_start",
        documentation=api.tr(
            "variable.dance_start",
            "The start time (in milliseconds) of the first time through the dance in a called folk dance."
        ),
        title=api.tr("variable.title.dance_start", "Dance Start Time"),
    )

    api.register_script_variable(
        name="dance_times",
        documentation=api.tr(
            "variable.dance_times",
            (
                "The number of complete times through the dance excluding any intro, outro, or potatoes for a "
                "called folk dance. The exact definition will depend on the type of dance."
            )
        ),
        title=api.tr("variable.title.dance_times", "Dance Times"),
    )

    api.register_script_variable(
        name="dance_title",
        documentation=api.tr(
            "variable.dance_title",
            "The name of the dance or dances being called for called folk dances."
        ),
        title=api.tr("variable.title.dance_title", "Dance Title"),
    )


def disable() -> None:
    """Called when the plugin is disabled."""
    pass
