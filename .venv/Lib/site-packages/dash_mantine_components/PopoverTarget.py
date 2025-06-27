# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class PopoverTarget(Component):
    """A PopoverTarget component.
PopoverTarget

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Content.

- boxWrapperProps (dict; optional):
    Target box wrapper props.

    `boxWrapperProps` is a dict with keys:

    - top (string | number; optional)

    - right (string | number; optional)

    - bottom (string | number; optional)

    - left (string | number; optional)

    - className (string; optional):
        Class added to the root element, if applicable.

    - style (optional):
        Inline style added to root component element, can subscribe to
        theme defined on MantineProvider.

    - hiddenFrom (optional):
        Breakpoint above which the component is hidden with `display:
        none`.

    - visibleFrom (optional):
        Breakpoint below which the component is hidden with `display:
        none`.

    - lightHidden (boolean; optional):
        Determines whether component should be hidden in light color
        scheme with `display: none`.

    - darkHidden (boolean; optional):
        Determines whether component should be hidden in dark color
        scheme with `display: none`.

    - mod (string; optional):
        Element modifiers transformed into `data-` attributes, for
        example, `{ 'data-size': 'xl' }`, falsy values are removed.

    - m (number; optional):
        Margin, theme key: theme.spacing.

    - my (number; optional):
        MarginBlock, theme key: theme.spacing.

    - mx (number; optional):
        MarginInline, theme key: theme.spacing.

    - mt (number; optional):
        MarginTop, theme key: theme.spacing.

    - mb (number; optional):
        MarginBottom, theme key: theme.spacing.

    - ms (number; optional):
        MarginInlineStart, theme key: theme.spacing.

    - me (number; optional):
        MarginInlineEnd, theme key: theme.spacing.

    - ml (number; optional):
        MarginLeft, theme key: theme.spacing.

    - mr (number; optional):
        MarginRight, theme key: theme.spacing.

    - p (number; optional):
        Padding, theme key: theme.spacing.

    - py (number; optional):
        PaddingBlock, theme key: theme.spacing.

    - px (number; optional):
        PaddingInline, theme key: theme.spacing.

    - pt (number; optional):
        PaddingTop, theme key: theme.spacing.

    - pb (number; optional):
        PaddingBottom, theme key: theme.spacing.

    - ps (number; optional):
        PaddingInlineStart, theme key: theme.spacing.

    - pe (number; optional):
        PaddingInlineEnd, theme key: theme.spacing.

    - pl (number; optional):
        PaddingLeft, theme key: theme.spacing.

    - pr (number; optional):
        PaddingRight, theme key: theme.spacing.

    - bd (string | number; optional):
        Border.

    - bg (optional):
        Background, theme key: theme.colors.

    - c (optional):
        Color.

    - opacity (optional)

    - ff (optional):
        FontFamily.

    - fz (number; optional):
        FontSize, theme key: theme.fontSizes.

    - fw (optional):
        FontWeight.

    - lts (string | number; optional):
        LetterSpacing.

    - ta (optional):
        TextAlign.

    - lh (number; optional):
        LineHeight, theme key: lineHeights.

    - fs (optional):
        FontStyle.

    - tt (optional):
        TextTransform.

    - td (string | number; optional):
        TextDecoration.

    - w (string | number; optional):
        Width, theme key: theme.spacing.

    - miw (string | number; optional):
        MinWidth, theme key: theme.spacing.

    - maw (string | number; optional):
        MaxWidth, theme key: theme.spacing.

    - h (string | number; optional):
        Height, theme key: theme.spacing.

    - mih (string | number; optional):
        MinHeight, theme key: theme.spacing.

    - mah (string | number; optional):
        MaxHeight, theme key: theme.spacing.

    - bgsz (string | number; optional):
        BackgroundSize.

    - bgp (string | number; optional):
        BackgroundPosition.

    - bgr (optional):
        BackgroundRepeat.

    - bga (optional):
        BackgroundAttachment.

    - pos (optional):
        Position.

    - inset (string | number; optional)

    - display (optional)

    - flex (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'PopoverTarget'
    BoxWrapperProps = TypedDict(
        "BoxWrapperProps",
            {
            "top": NotRequired[typing.Union[str, NumberType]],
            "right": NotRequired[typing.Union[str, NumberType]],
            "bottom": NotRequired[typing.Union[str, NumberType]],
            "left": NotRequired[typing.Union[str, NumberType]],
            "className": NotRequired[str],
            "style": NotRequired[typing.Union[typing.Any]],
            "hiddenFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "visibleFrom": NotRequired[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "lightHidden": NotRequired[bool],
            "darkHidden": NotRequired[bool],
            "mod": NotRequired[typing.Union[str]],
            "m": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "my": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mx": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ms": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "me": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ml": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "mr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "p": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "py": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "px": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pt": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pb": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "ps": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pe": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pl": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "pr": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]],
            "bd": NotRequired[typing.Union[str, NumberType]],
            "bg": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "c": NotRequired[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]],
            "opacity": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]],
            "ff": NotRequired[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]],
            "fz": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fw": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]],
            "lts": NotRequired[typing.Union[str, NumberType]],
            "ta": NotRequired[typing.Union[Literal["right"], Literal["left"], Literal["end"], Literal["start"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["center"], Literal["-webkit-match-parent"], Literal["justify"], Literal["match-parent"]]],
            "lh": NotRequired[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]],
            "fs": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["normal"], Literal["italic"], Literal["oblique"]]],
            "tt": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["capitalize"], Literal["full-size-kana"], Literal["full-width"], Literal["lowercase"], Literal["uppercase"]]],
            "td": NotRequired[typing.Union[str, NumberType]],
            "w": NotRequired[typing.Union[str, NumberType]],
            "miw": NotRequired[typing.Union[str, NumberType]],
            "maw": NotRequired[typing.Union[str, NumberType]],
            "h": NotRequired[typing.Union[str, NumberType]],
            "mih": NotRequired[typing.Union[str, NumberType]],
            "mah": NotRequired[typing.Union[str, NumberType]],
            "bgsz": NotRequired[typing.Union[str, NumberType]],
            "bgp": NotRequired[typing.Union[str, NumberType]],
            "bgr": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["no-repeat"], Literal["repeat"], Literal["repeat-x"], Literal["repeat-y"], Literal["round"], Literal["space"]]],
            "bga": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["local"], Literal["scroll"]]],
            "pos": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["absolute"], Literal["fixed"], Literal["-webkit-sticky"], Literal["relative"], Literal["static"], Literal["sticky"]]],
            "inset": NotRequired[typing.Union[str, NumberType]],
            "display": NotRequired[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["flex"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]],
            "flex": NotRequired[typing.Union[str, NumberType]]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        boxWrapperProps: typing.Optional["BoxWrapperProps"] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'boxWrapperProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'boxWrapperProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(PopoverTarget, self).__init__(children=children, **args)

setattr(PopoverTarget, "__init__", _explicitize_args(PopoverTarget.__init__))
