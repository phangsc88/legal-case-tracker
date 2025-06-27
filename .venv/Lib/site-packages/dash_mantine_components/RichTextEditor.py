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


class RichTextEditor(Component):
    """A RichTextEditor component.
RichTextEditor

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- aria-* (string; optional):
    Wild card aria attributes.

- bd (string | number; optional):
    Border.

- bg (optional):
    Background, theme key: theme.colors.

- bga (optional):
    BackgroundAttachment.

- bgp (string | number; optional):
    BackgroundPosition.

- bgr (optional):
    BackgroundRepeat.

- bgsz (string | number; optional):
    BackgroundSize.

- bottom (string | number; optional)

- c (optional):
    Color.

- className (string; optional):
    Class added to the root element, if applicable.

- classNames (dict; optional):
    Adds class names to Mantine components.

- darkHidden (boolean; optional):
    Determines whether component should be hidden in dark color scheme
    with `display: none`.

- data-* (string; optional):
    Wild card data attributes.

- debounce (number; optional):
    If True, changes will be sent back to Dash only when losing focus.
    If False, data will be sent on every change. If a number, data
    will be sent when the value has been stable for that number of
    milliseconds.

- display (optional)

- extensions (list; optional):
    List of extensions to be loaded by the editor. Each item can be
    either a string with the extension name (e.g. 'Color') or an
    object with the extension name as key and options as value (e.g.
    {'TextAlign': {'types': ['heading', 'paragraph']}}).
    ['StarterKit', 'Underline', 'Link', 'Superscript', 'Subscript',
    'Highlight', 'Table', 'TableCell', 'TableHeader', 'TableRow',
    {'Placeholder': {'placeholder': 'Write or paste content
    here...'}}, {'TextAlign': {'types': ['heading', 'paragraph']}},
    'Color', 'TextStyle', 'Image'] by default.

- ff (optional):
    FontFamily.

- flex (string | number; optional)

- fs (optional):
    FontStyle.

- fw (optional):
    FontWeight.

- fz (number; optional):
    FontSize, theme key: theme.fontSizes.

- h (string | number; optional):
    Height, theme key: theme.spacing.

- hiddenFrom (optional):
    Breakpoint above which the component is hidden with `display:
    none`.

- html (string; optional):
    HTML string representation of the editor content. Affected by
    debounce. If both json and html are provided, json takes
    precedence.

- inset (string | number; optional)

- json (dict; optional):
    JSON object (ProseMirror) representation of the editor content.
    Affected by debounce. If both json and html are provide, json
    takes precedence.

- labels (dict; optional):
    Labels that are used in controls. If not set, default labels are
    used.

    `labels` is a dict with keys:

    - boldControlLabel (string; optional):
        RichTextEditor.Bold control aria-label.

    - hrControlLabel (string; optional):
        RichTextEditor.Hr control aria-label.

    - italicControlLabel (string; optional):
        RichTextEditor.Italic control aria-label.

    - underlineControlLabel (string; optional):
        RichTextEditor.Underline control aria-label.

    - strikeControlLabel (string; optional):
        RichTextEditor.Strike control aria-label.

    - clearFormattingControlLabel (string; optional):
        RichTextEditor.ClearFormatting control aria-label.

    - linkControlLabel (string; optional):
        RichTextEditor.Link control aria-label.

    - unlinkControlLabel (string; optional):
        RichTextEditor.Unlink control aria-label.

    - bulletListControlLabel (string; optional):
        RichTextEditor.BulletList control aria-label.

    - orderedListControlLabel (string; optional):
        RichTextEditor.OrderedList control aria-label.

    - h1ControlLabel (string; optional):
        RichTextEditor.H1 control aria-label.

    - h2ControlLabel (string; optional):
        RichTextEditor.H2 control aria-label.

    - h3ControlLabel (string; optional):
        RichTextEditor.H3 control aria-label.

    - h4ControlLabel (string; optional):
        RichTextEditor.H4 control aria-label.

    - h5ControlLabel (string; optional):
        RichTextEditor.H5 control aria-label.

    - h6ControlLabel (string; optional):
        RichTextEditor.H6 control aria-label.

    - blockquoteControlLabel (string; optional):
        RichTextEditor.Blockquote control aria-label.

    - alignLeftControlLabel (string; optional):
        RichTextEditor.AlignLeft control aria-label.

    - alignCenterControlLabel (string; optional):
        RichTextEditor.AlignCenter control aria-label.

    - alignRightControlLabel (string; optional):
        RichTextEditor.AlignRight control aria-label.

    - alignJustifyControlLabel (string; optional):
        RichTextEditor.AlignJustify control aria-label.

    - codeControlLabel (string; optional):
        RichTextEditor.Code control aria-label.

    - codeBlockControlLabel (string; optional):
        RichTextEditor.CodeBlock control aria-label.

    - subscriptControlLabel (string; optional):
        RichTextEditor.Subscript control aria-label.

    - superscriptControlLabel (string; optional):
        RichTextEditor.Superscript control aria-label.

    - colorPickerControlLabel (string; optional):
        RichTextEditor.ColorPicker control aria-label.

    - unsetColorControlLabel (string; optional):
        RichTextEditor.UnsetColor control aria-label.

    - highlightControlLabel (string; optional):
        RichTextEditor.Highlight control aria-label.

    - undoControlLabel (string; optional):
        RichTextEditor.Undo control aria-label.

    - redoControlLabel (string; optional):
        RichTextEditor.Redo control aria-label.

    - linkEditorInputLabel (string; optional):
        Aria-label for link editor url input.

    - linkEditorInputPlaceholder (string; optional):
        Placeholder for link editor url input.

    - linkEditorExternalLink (string; optional):
        Content of external button tooltip in link editor when the
        link was chosen to open in a new tab.

    - linkEditorInternalLink (string; optional):
        Content of external button tooltip in link editor when the
        link was chosen to open in the same tab.

    - linkEditorSave (string; optional):
        Save button content in link editor.

    - colorPickerCancel (string; optional):
        Cancel button title text in color picker control.

    - colorPickerClear (string; optional):
        Clear button title text in color picker control.

    - colorPickerColorPicker (string; optional):
        Color picker button title text in color picker control.

    - colorPickerPalette (string; optional):
        Palette button title text in color picker control.

    - colorPickerSave (string; optional):
        Save button title text in color picker control.

    - tasksControlLabel (string; optional):
        Aria-label for task list control.

    - tasksSinkLabel (string; optional):
        Aria-label for task list sink task.

    - tasksLiftLabel (string; optional):
        Aria-label for task list lift task.

    - colorControlLabel (string; optional):
        An string containing '{color}' (replaced with the color) to go
        the color control label.

    - colorPickerColorLabel (string; optional):
        An string containing '{color}' (replaced with the color) to go
        the color picker control label.

- left (string | number; optional)

- lh (number; optional):
    LineHeight, theme key: lineHeights.

- lightHidden (boolean; optional):
    Determines whether component should be hidden in light color
    scheme with `display: none`.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer. For use with dash<3.

    `loading_state` is a dict with keys:

    - is_loading (boolean; required):
        Determines if the component is loading or not.

    - prop_name (string; required):
        Holds which property is loading.

    - component_name (string; required):
        Holds the name of the component that is loading.

- lts (string | number; optional):
    LetterSpacing.

- m (number; optional):
    Margin, theme key: theme.spacing.

- mah (string | number; optional):
    MaxHeight, theme key: theme.spacing.

- maw (string | number; optional):
    MaxWidth, theme key: theme.spacing.

- mb (number; optional):
    MarginBottom, theme key: theme.spacing.

- me (number; optional):
    MarginInlineEnd, theme key: theme.spacing.

- mih (string | number; optional):
    MinHeight, theme key: theme.spacing.

- miw (string | number; optional):
    MinWidth, theme key: theme.spacing.

- ml (number; optional):
    MarginLeft, theme key: theme.spacing.

- mod (string; optional):
    Element modifiers transformed into `data-` attributes, for
    example, `{ 'data-size': 'xl' }`, falsy values are removed.

- mr (number; optional):
    MarginRight, theme key: theme.spacing.

- ms (number; optional):
    MarginInlineStart, theme key: theme.spacing.

- mt (number; optional):
    MarginTop, theme key: theme.spacing.

- mx (number; optional):
    MarginInline, theme key: theme.spacing.

- my (number; optional):
    MarginBlock, theme key: theme.spacing.

- n_blur (number; optional):
    An integer that represents the number of times that this element
    has lost focus.

- opacity (optional)

- p (number; optional):
    Padding, theme key: theme.spacing.

- pb (number; optional):
    PaddingBottom, theme key: theme.spacing.

- pe (number; optional):
    PaddingInlineEnd, theme key: theme.spacing.

- persisted_props (list of strings; optional):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; optional):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pl (number; optional):
    PaddingLeft, theme key: theme.spacing.

- pos (optional):
    Position.

- pr (number; optional):
    PaddingRight, theme key: theme.spacing.

- ps (number; optional):
    PaddingInlineStart, theme key: theme.spacing.

- pt (number; optional):
    PaddingTop, theme key: theme.spacing.

- px (number; optional):
    PaddingInline, theme key: theme.spacing.

- py (number; optional):
    PaddingBlock, theme key: theme.spacing.

- right (string | number; optional)

- selected (string; optional):
    Currently selected text. Affected by debounce.

- styles (boolean | number | string | dict | list; optional):
    Mantine styles API.

- ta (optional):
    TextAlign.

- tabIndex (number; optional):
    tab-index.

- td (string | number; optional):
    TextDecoration.

- toolbar (dict; optional):
    Toolbar property definition. Empty by default.

    `toolbar` is a dict with keys:

    - sticky (boolean; optional):
        Determines whether `position: sticky` styles should be added
        to the toolbar, `False` by default.

    - stickyOffset (string | number; optional):
        Sets top style to offset elements with fixed position, `0` by
        default.

    - controlsGroups (list of lists; optional):
        Groups of controls to be displayed in the toolbar. Each item
        can be either a string with the control name (e.g. 'Bold') or
        an object with the control name as key and options as value
        (e.g. {'Color': {'color': 'red'}}). Empty by default.

- top (string | number; optional)

- tt (optional):
    TextTransform.

- unstyled (boolean; optional):
    Remove all Mantine styling from the component.

- variant (a value equal to: 'default', 'subtle'; optional):
    Variant of the editor.

- visibleFrom (optional):
    Breakpoint below which the component is hidden with `display:
    none`.

- w (string | number; optional):
    Width, theme key: theme.spacing.

- withCodeHighlightStyles (boolean; optional):
    Determines whether code highlight styles should be added, True by
    default.

- withTypographyStyles (boolean; optional):
    Determines whether typography styles should be added, True by
    default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mantine_components'
    _type = 'RichTextEditor'
    Extensions_StarterKit = TypedDict(
        "Extensions_StarterKit",
            {

        }
    )

    Extensions_Underline = TypedDict(
        "Extensions_Underline",
            {

        }
    )

    Extensions_Link = TypedDict(
        "Extensions_Link",
            {

        }
    )

    Extensions_Superscript = TypedDict(
        "Extensions_Superscript",
            {

        }
    )

    Extensions_Subscript = TypedDict(
        "Extensions_Subscript",
            {

        }
    )

    Extensions_Highlight = TypedDict(
        "Extensions_Highlight",
            {

        }
    )

    Extensions_TextAlign = TypedDict(
        "Extensions_TextAlign",
            {

        }
    )

    Extensions_TextStyle = TypedDict(
        "Extensions_TextStyle",
            {

        }
    )

    Extensions_Table = TypedDict(
        "Extensions_Table",
            {

        }
    )

    Extensions_TableCell = TypedDict(
        "Extensions_TableCell",
            {

        }
    )

    Extensions_TableRow = TypedDict(
        "Extensions_TableRow",
            {

        }
    )

    Extensions_TableHeader = TypedDict(
        "Extensions_TableHeader",
            {

        }
    )

    Extensions_Placeholder = TypedDict(
        "Extensions_Placeholder",
            {

        }
    )

    Extensions_Image = TypedDict(
        "Extensions_Image",
            {

        }
    )

    Extensions_Color = TypedDict(
        "Extensions_Color",
            {

        }
    )

    Extensions = TypedDict(
        "Extensions",
            {
            "StarterKit": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_StarterKit"]],
            "Underline": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Underline"]],
            "Link": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Link"]],
            "Superscript": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Superscript"]],
            "Subscript": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Subscript"]],
            "Highlight": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Highlight"]],
            "TextAlign": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_TextAlign"]],
            "TextStyle": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_TextStyle"]],
            "Table": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Table"]],
            "TableCell": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_TableCell"]],
            "TableRow": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_TableRow"]],
            "TableHeader": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_TableHeader"]],
            "Placeholder": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Placeholder"]],
            "Image": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Image"]],
            "Color": NotRequired[typing.Dict[typing.Union[str, float, int], "Extensions_Color"]]
        }
    )

    Toolbar = TypedDict(
        "Toolbar",
            {
            "sticky": NotRequired[bool],
            "stickyOffset": NotRequired[typing.Union[str, NumberType]],
            "controlsGroups": NotRequired[typing.Sequence[typing.Sequence[typing.Union[Literal["Underline"], Literal["Link"], Literal["Superscript"], Literal["Subscript"], Literal["Highlight"], Literal["Color"], Literal["Bold"], Literal["Italic"], Literal["Strikethrough"], Literal["ClearFormatting"], Literal["Code"], Literal["H1"], Literal["H2"], Literal["H3"], Literal["H4"], Literal["H5"], Literal["H6"], Literal["CodeBlock"], Literal["Blockquote"], Literal["Hr"], Literal["BulletList"], Literal["OrderedList"], Literal["Unlink"], Literal["AlignLeft"], Literal["AlignCenter"], Literal["AlignJustify"], Literal["AlignRight"], Literal["Undo"], Literal["Redo"], Literal["ColorPicker"], Literal["UnsetColor"]]]]]
        }
    )

    Labels = TypedDict(
        "Labels",
            {
            "boldControlLabel": NotRequired[str],
            "hrControlLabel": NotRequired[str],
            "italicControlLabel": NotRequired[str],
            "underlineControlLabel": NotRequired[str],
            "strikeControlLabel": NotRequired[str],
            "clearFormattingControlLabel": NotRequired[str],
            "linkControlLabel": NotRequired[str],
            "unlinkControlLabel": NotRequired[str],
            "bulletListControlLabel": NotRequired[str],
            "orderedListControlLabel": NotRequired[str],
            "h1ControlLabel": NotRequired[str],
            "h2ControlLabel": NotRequired[str],
            "h3ControlLabel": NotRequired[str],
            "h4ControlLabel": NotRequired[str],
            "h5ControlLabel": NotRequired[str],
            "h6ControlLabel": NotRequired[str],
            "blockquoteControlLabel": NotRequired[str],
            "alignLeftControlLabel": NotRequired[str],
            "alignCenterControlLabel": NotRequired[str],
            "alignRightControlLabel": NotRequired[str],
            "alignJustifyControlLabel": NotRequired[str],
            "codeControlLabel": NotRequired[str],
            "codeBlockControlLabel": NotRequired[str],
            "subscriptControlLabel": NotRequired[str],
            "superscriptControlLabel": NotRequired[str],
            "colorPickerControlLabel": NotRequired[str],
            "unsetColorControlLabel": NotRequired[str],
            "highlightControlLabel": NotRequired[str],
            "undoControlLabel": NotRequired[str],
            "redoControlLabel": NotRequired[str],
            "linkEditorInputLabel": NotRequired[str],
            "linkEditorInputPlaceholder": NotRequired[str],
            "linkEditorExternalLink": NotRequired[str],
            "linkEditorInternalLink": NotRequired[str],
            "linkEditorSave": NotRequired[str],
            "colorPickerCancel": NotRequired[str],
            "colorPickerClear": NotRequired[str],
            "colorPickerColorPicker": NotRequired[str],
            "colorPickerPalette": NotRequired[str],
            "colorPickerSave": NotRequired[str],
            "tasksControlLabel": NotRequired[str],
            "tasksSinkLabel": NotRequired[str],
            "tasksLiftLabel": NotRequired[str],
            "colorControlLabel": NotRequired[str],
            "colorPickerColorLabel": NotRequired[str]
        }
    )

    LoadingState = TypedDict(
        "LoadingState",
            {
            "is_loading": bool,
            "prop_name": str,
            "component_name": str
        }
    )


    def __init__(
        self,
        json: typing.Optional[dict] = None,
        html: typing.Optional[str] = None,
        selected: typing.Optional[str] = None,
        debounce: typing.Optional[typing.Union[NumberType]] = None,
        n_blur: typing.Optional[NumberType] = None,
        variant: typing.Optional[Literal["default", "subtle"]] = None,
        extensions: typing.Optional[typing.Sequence[typing.Union[Literal["StarterKit"], Literal["Underline"], Literal["Link"], Literal["Superscript"], Literal["Subscript"], Literal["Highlight"], Literal["TextAlign"], Literal["TextStyle"], Literal["Table"], Literal["TableCell"], Literal["TableRow"], Literal["TableHeader"], Literal["Placeholder"], Literal["Image"], Literal["Color"]]]] = None,
        toolbar: typing.Optional["Toolbar"] = None,
        withCodeHighlightStyles: typing.Optional[bool] = None,
        withTypographyStyles: typing.Optional[bool] = None,
        labels: typing.Optional["Labels"] = None,
        className: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        hiddenFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        visibleFrom: typing.Optional[typing.Union[Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        lightHidden: typing.Optional[bool] = None,
        darkHidden: typing.Optional[bool] = None,
        mod: typing.Optional[typing.Union[str]] = None,
        m: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        my: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mx: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mt: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mb: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ms: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        me: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ml: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        mr: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        p: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        py: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        px: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pt: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pb: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        ps: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pe: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pl: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        pr: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"]]] = None,
        bd: typing.Optional[typing.Union[str, NumberType]] = None,
        bg: typing.Optional[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]] = None,
        c: typing.Optional[typing.Union[Literal["blue"], Literal["cyan"], Literal["gray"], Literal["green"], Literal["indigo"], Literal["lime"], Literal["orange"], Literal["pink"], Literal["red"], Literal["teal"], Literal["violet"], Literal["yellow"], Literal["dark"], Literal["grape"]]] = None,
        opacity: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"]]] = None,
        ff: typing.Optional[typing.Union[Literal["monospace"], Literal["text"], Literal["heading"]]] = None,
        fz: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
        fw: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["bold"], Literal["normal"], Literal["bolder"], Literal["lighter"]]] = None,
        lts: typing.Optional[typing.Union[str, NumberType]] = None,
        ta: typing.Optional[typing.Union[Literal["left"], Literal["right"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["-webkit-match-parent"], Literal["center"], Literal["end"], Literal["justify"], Literal["match-parent"], Literal["start"]]] = None,
        lh: typing.Optional[typing.Union[NumberType, Literal["xs"], Literal["sm"], Literal["md"], Literal["lg"], Literal["xl"], Literal["h1"], Literal["h2"], Literal["h3"], Literal["h4"], Literal["h5"], Literal["h6"]]] = None,
        fs: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["normal"], Literal["italic"], Literal["oblique"]]] = None,
        tt: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["capitalize"], Literal["full-size-kana"], Literal["full-width"], Literal["lowercase"], Literal["uppercase"]]] = None,
        td: typing.Optional[typing.Union[str, NumberType]] = None,
        w: typing.Optional[typing.Union[str, NumberType]] = None,
        miw: typing.Optional[typing.Union[str, NumberType]] = None,
        maw: typing.Optional[typing.Union[str, NumberType]] = None,
        h: typing.Optional[typing.Union[str, NumberType]] = None,
        mih: typing.Optional[typing.Union[str, NumberType]] = None,
        mah: typing.Optional[typing.Union[str, NumberType]] = None,
        bgsz: typing.Optional[typing.Union[str, NumberType]] = None,
        bgp: typing.Optional[typing.Union[str, NumberType]] = None,
        bgr: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["no-repeat"], Literal["repeat"], Literal["repeat-x"], Literal["repeat-y"], Literal["round"], Literal["space"]]] = None,
        bga: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["local"], Literal["scroll"]]] = None,
        pos: typing.Optional[typing.Union[Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["fixed"], Literal["-webkit-sticky"], Literal["absolute"], Literal["relative"], Literal["static"], Literal["sticky"]]] = None,
        top: typing.Optional[typing.Union[str, NumberType]] = None,
        left: typing.Optional[typing.Union[str, NumberType]] = None,
        bottom: typing.Optional[typing.Union[str, NumberType]] = None,
        right: typing.Optional[typing.Union[str, NumberType]] = None,
        inset: typing.Optional[typing.Union[str, NumberType]] = None,
        display: typing.Optional[typing.Union[Literal["flex"], Literal["-moz-initial"], Literal["inherit"], Literal["initial"], Literal["revert"], Literal["revert-layer"], Literal["unset"], Literal["none"], Literal["block"], Literal["inline"], Literal["run-in"], Literal["-ms-flexbox"], Literal["-ms-grid"], Literal["-webkit-flex"], Literal["flow"], Literal["flow-root"], Literal["grid"], Literal["ruby"], Literal["table"], Literal["ruby-base"], Literal["ruby-base-container"], Literal["ruby-text"], Literal["ruby-text-container"], Literal["table-caption"], Literal["table-cell"], Literal["table-column"], Literal["table-column-group"], Literal["table-footer-group"], Literal["table-header-group"], Literal["table-row"], Literal["table-row-group"], Literal["-ms-inline-flexbox"], Literal["-ms-inline-grid"], Literal["-webkit-inline-flex"], Literal["inline-block"], Literal["inline-flex"], Literal["inline-grid"], Literal["inline-list-item"], Literal["inline-table"], Literal["contents"], Literal["list-item"]]] = None,
        flex: typing.Optional[typing.Union[str, NumberType]] = None,
        classNames: typing.Optional[dict] = None,
        styles: typing.Optional[typing.Any] = None,
        unstyled: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        tabIndex: typing.Optional[NumberType] = None,
        loading_state: typing.Optional["LoadingState"] = None,
        persistence: typing.Optional[typing.Union[str, NumberType]] = None,
        persisted_props: typing.Optional[typing.Sequence[str]] = None,
        persistence_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'display', 'extensions', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'html', 'inset', 'json', 'labels', 'left', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'selected', 'style', 'styles', 'ta', 'tabIndex', 'td', 'toolbar', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCodeHighlightStyles', 'withTypographyStyles']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['id', 'aria-*', 'bd', 'bg', 'bga', 'bgp', 'bgr', 'bgsz', 'bottom', 'c', 'className', 'classNames', 'darkHidden', 'data-*', 'debounce', 'display', 'extensions', 'ff', 'flex', 'fs', 'fw', 'fz', 'h', 'hiddenFrom', 'html', 'inset', 'json', 'labels', 'left', 'lh', 'lightHidden', 'loading_state', 'lts', 'm', 'mah', 'maw', 'mb', 'me', 'mih', 'miw', 'ml', 'mod', 'mr', 'ms', 'mt', 'mx', 'my', 'n_blur', 'opacity', 'p', 'pb', 'pe', 'persisted_props', 'persistence', 'persistence_type', 'pl', 'pos', 'pr', 'ps', 'pt', 'px', 'py', 'right', 'selected', 'style', 'styles', 'ta', 'tabIndex', 'td', 'toolbar', 'top', 'tt', 'unstyled', 'variant', 'visibleFrom', 'w', 'withCodeHighlightStyles', 'withTypographyStyles']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(RichTextEditor, self).__init__(**args)

setattr(RichTextEditor, "__init__", _explicitize_args(RichTextEditor.__init__))
